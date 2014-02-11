/*
 * Logic for D3 visualization of Enron Data Set
 * For CS 467, Spring 2014.
 * Authors: Jay Bensal, Raj Ramamurthy
 */

/* Data storage */

/* Load in the data */
var loadData = function() {
  
  d3.json('', function () {
    // callback function here
    dataIsLoaded();
  });
};

/* The data is loaded at this point. */
var dataIsLoaded = function() {
  console.log('All data loaded.');
  makeGraph();
};

/* Make a scatterplot graph for the life expectancies*/
var makeGraph = function(){
  

}; // end makeGraph function
