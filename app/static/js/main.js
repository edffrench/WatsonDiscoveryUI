
const searchbar = document.getElementById('search-bar')
const searchbtn = document.getElementById('search-btn1')

const searchquery = document.getElementById('search-query')

searchbar.addEventListener('keydown', checkKeyPress, false);
searchbtn.addEventListener('click', click, false);

function checkKeyPress(key){
    if (key.keyCode == '13'){
        window.location.href = 'http://127.0.0.1:5000/search-page?query=' + searchquery.value;
        
    }
}

function click(searchbtn){
        window.location.href = 'http://127.0.0.1:5000/search-page?query=' + searchquery.value;
    
}

