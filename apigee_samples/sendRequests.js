// search is a query parameter with a comma-separated list of topics to be searched
var searchParam = context.getVariable("request.queryparam.search");
if (searchParam === null || searchParam.length === 0) {
    throw("search query parameter not found");
}
var search = searchParam.split(",");
print("search=" + search); 
// call max 5 in parallel
var maxCalls = search.length;
if (maxCalls > 5) {
    maxCalls = 5;
}
print("maxCalls=" + maxCalls);
// URL to the Google Books API
var url="https://www.googleapis.com/books/v1/volumes?country=US&q=subject:";
var searchTerms = [];
// for each search term, call the Google API
for (var i=0; i < maxCalls; i++) {
    var searchTerm = search[i];
    print("" + i + ": " + searchTerm);
    print("GET " + url + ""+searchTerm);
    var req = httpClient.get(url+searchTerm);
    // store the request in a session for later retrieval
    searchTerms.push(searchTerm);
    context.session["searchTerm:" + searchTerm] = req;
}
context.session["searchTerms"] = searchTerms;
print("done sending the requests");