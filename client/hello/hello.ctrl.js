angular.module('app')
    .controller('HelloCtrl', function ($scope, HelloSvc) {
        $scope.$watch('name', function () {
            HelloSvc.fetchGreeting({name: $scope.name}, function (data) {
                $scope.greeting = data.message;
            });
        });
    });
