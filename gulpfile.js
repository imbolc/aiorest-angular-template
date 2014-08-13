var gulp = require('gulp');
var concat = require('gulp-concat');
var sourcemaps = require('gulp-sourcemaps');
var uglify = require('gulp-uglify');
var ngAnnotate = require('gulp-ng-annotate');
var shell = require('gulp-shell');
var plumber = require('gulp-plumber');


gulp.task('js', function () {
    gulp.src(['client/app.js', 'client/**/*.js'])
    .pipe(plumber())
    .pipe(sourcemaps.init())
    .pipe(concat('app.js'))
    .pipe(ngAnnotate())
    .pipe(uglify())
    .pipe(sourcemaps.write())
    .pipe(gulp.dest('./static/build'));
});

gulp.task('watch', ['js'], function () {
    gulp.watch('client/**/*.js', ['js']);
});

gulp.task('dev_server', shell.task([
    ('nodemon ./app.py -V --exec "var/env/bin/python"' +
    // ' --watch "*.py" --watch "templates/*.html"')
    ' --ext "py html" --ignore "static"')
]));

gulp.task('default', ['dev_server', 'watch'], function() {

});
