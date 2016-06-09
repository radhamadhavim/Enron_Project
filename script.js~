angular.module('enron', [])
   .controller('enronController', ['$scope','$http', '$log', function ($scope,$http,$log) { 
    $scope.from="me@example.com"
    $scope.emailFormat =/^[a-z]+[a-z0-9._]+@[a-z]+\.[a-z.]{2,5}$/;  
    
    $scope.email = function(from,to) { $scope.email = $http.get  ('http://localhost:5000/predict', 
                                              {params:{"from": from, "to": to}}).
        success(function(response) {                        
          $scope.ToList = response.predictions;                   
                                  
       });    
 
     };     
}]);
  
    

