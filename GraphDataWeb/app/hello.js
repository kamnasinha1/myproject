/**
 * Created by root on 3/23/17.
 */
angular.module('demo', [])
.controller('Hello', function($scope, $http) {
    $http.get('http://localhost:5000').
        then(function(response) {
            $scope.greeting = response.data;

        });
});
