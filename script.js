$(document).ready(function () {
    $('#user-form').on('submit', function (event) {
        event.preventDefault(); // Prevent the default form submission

        let query = $('#q').val().trim(); // Get the input value

        if (query) {
            // Append the searched ingredient to the history section
            $('#ingredient-search-history').append('<p>' + query + '</p>'); 
            displaySearchResults(query); // Call the function to display the search results

            // Send an AJAX request to the Flask backend
            $.ajax({
                url: '/search', // The endpoint we created in Flask
                method: 'POST',
                data: { ingredients: query }, // Send the ingredients as form data (not JSON)
                success: function (data) {
                    // Assuming 'data' contains the recipe results
                    $('#recipe-results').empty(); // Clear previous results
                    if (data.recipes.length > 0) {
                        data.recipes.forEach(function (recipe) {
                            // Append each recipe (you can customize the format for displaying)
                            $('#recipe-results').append('<div class="recipe-item"><h3>' + recipe.name + '</h3><p>' + recipe.instructions + '</p><p>Ingredients: ' + recipe.ingredients.join(', ') + '</p></div>');
                        });
                    } else {
                        $('#recipe-results').html('<p>No recipes found.</p>');
                    }
                },
                error: function () {
                    $('#recipe-results').html('<p>Error retrieving recipes.</p>');
                }
            });

            $('#q').val(''); // Clear input field after submission
        } else {
            alert("Please enter ingredients");
        }
    });

    // Define the function to display the search results message
    function displaySearchResults(query) {
        $('#recipe-results').html('<p>Searching for recipes with ' + query + '...</p>');
    }
});
