const countrySearchWord = {'France': 'French', 'Thailand': 'Thai', 'Italy': 'Italian', 
'India': 'Indian', 'Spain': 'Spanish', "Greece": 'Greek', 'Mexico': 'Mexican', 
'Turkey': 'Turkey', 'Argentina': 'Argentina', 'Portugal': 'Portugal'};

// DOM elements to set event listeners
const countryList = document.querySelectorAll(".country.list-group-item.list-group-item-action");

// add event listener for each country in country list-group
for (let i = 0; i<countryList.length; i++) {
    countryList[i].addEventListener("click", function(){
        makeRequestForCountryRecipe(countryList[i].innerText)
    });
}

function makeRequestForCountryRecipe(country) {
    // send a fetch request to server POST with key value in countrySearchWord
    // https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
    const data = {"country": countrySearchWord[country]};
    fetch('/recipes_for_country', {
    method: 'POST', // or 'PUT'
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
    });
}


