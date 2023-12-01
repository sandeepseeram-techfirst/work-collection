var searchTerms = context.session["searchTerms"];
var resp = [];
// Iterate for each search term 
for (var i=0; i < searchTerms.length; i++) { 
    // retrieve request object from session 
    var searchTerm = searchTerms[i];
    req = context.session["searchTerm:" + searchTerm]; 
    req.waitForComplete();
    print("Got response for " + searchTerm);
    if (req.isSuccess()) {
        print("Success!");
        item = {
            query : searchTerm,
            result : JSON.parse(req.getResponse().content)
        };
    }
    else {
        print("Error: " + JSON.stringify(req.getError()));
        item = {
            query : searchTerm,
            result : null
        }
    }
    resp.push(item);
    print(item);
    // store JSONresponse in a temporary flow variable
    context.setVariable("bookResponses", JSON.stringify(resp));
}
print("done processing responses");