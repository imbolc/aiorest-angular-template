angular.module('app')
    .service('HelloSvc', function ($resource, cfg) {
        this.fetchGreeting = function () {
            return $resource(cfg.urls.hello).get.apply(this, arguments);
        };
    });
