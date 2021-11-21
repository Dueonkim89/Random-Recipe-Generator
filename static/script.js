const countrySearchWord = {'France': 'French', 'Thailand': 'Thai', 'Italy': 'Italian', 
'India': 'Indian', 'Spain': 'Spanish', "Greece": 'Greek', 'Mexico': 'Mexican', 
'Turkey': 'Turkey', 'Argentina': 'Argentina', 'Portugal': 'Portugal'};

// DOM elements to set event listeners
const countryList = document.querySelectorAll(".country.list-group-item.list-group-item-action");
const countrySubmitFormField = document.querySelector(".country-submit-form");
const countryChoice = document.querySelector(".country-list-form");
const recipeChoice = document.querySelector(".recipe-list-form");

// add event listener for each country in country list-group
for (let i = 0; i<countryList.length; i++) {
    countryList[i].addEventListener("click", function(){
        makeRequestForCountryRecipe(countryList[i].innerText)
    });
}

// add event listener for country selection form field
if (countrySubmitFormField) {
    // add form submit event listener for random country generation
    countrySubmitFormField.addEventListener('submit', function(event) {
        // get value from select dropdown
        selectMenuValue = document.querySelector('.form-select').value;
        // give warning if form field has null value
        if (selectMenuValue === "0") {
            event.preventDefault()
            alert("Please choose an option!")
            return;
        }
        // disable Submit Button
        disableSubmitButton()
    });
}

// add event listener for country choice form field
if (countryChoice) {
    // add form submit event listener for country choice
    countryChoice.addEventListener('submit', function(event) {
        // none of the country  radio buttons are checked
        if (!document.querySelector('input[name="countryRadios"]:checked')) {
            event.preventDefault()
            alert("Please choose a country!")
            return;
        }
        // disable Submit Button
        disableSubmitButton()
    });
}

// add event listener for recipe list form field
if (recipeChoice) {
    // add form submit event listener for recipe choice
    recipeChoice.addEventListener('submit', function(event) {
        // none of the country  radio buttons are checked
        if (!document.querySelector('input[name="recipeRadios"]:checked')) {
            event.preventDefault()
            alert("Please choose a recipe!")
            return;
        }
        // disable Submit Button
        disableSubmitButton()
    });
}

function disableSubmitButton() {
    // get submit button, change text and set to disabled
    const submitButton = document.querySelector('button[type="submit"]')
    submitButton.disabled = true;
    submitButton.innerText = "Loading Data...";
    submitButton.classList.remove("btn-secondary");
    submitButton.classList.add("btn-success")
}

// ABORT: forces web page to be SPA.
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