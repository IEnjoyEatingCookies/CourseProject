// Enable All Tooltips
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})

// Search on click
submitForm = (event, form) => {
    e.preventDefault();
    
    fetch('/search', {
      method: 'post',
      body: JSON.stringify({query : form.query.value})
    }).then((response) => {
      return response.json();
    }).then((data) => {
      //Success code goes here
    }).catch((err) => {
      //Failure
    });
}