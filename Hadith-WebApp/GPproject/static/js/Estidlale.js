const hadithText = document.querySelector(".hadithh")
hadithBtn = document.querySelector(".newhadithBtn");
loginBtn = document.querySelector(".loginBtn");
signupBtn = document.querySelector(".signupBtn");




var previousNumber;

function getRandomNumber() {
    var randomNumber;
        do {
            randomNumber = Math.floor(Math.random() * 201);
            } 
            while (randomNumber === previousNumber);
            previousNumber = randomNumber;
                return randomNumber;
}

function randomHadith(){
    fetch("https://api.hadith.gading.dev/books/bukhari?range=300-500").then(res => (res.json()).then(result =>
        {
            var randomNumber = getRandomNumber();
            hadithText.innerText = result["data"]["hadiths"][randomNumber]["arab"];
            
        }));
}

hadithBtn.addEventListener("click", randomHadith);


/*responsive*/

let menu = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');

menu.onclick = () => 
{
    menu.classList.toggle('bx-x');
    navbar.classList.toggle('active');
}

/*to remove the menu when click on any page*/
window.onscroll = () => 
{
    menu.classList.remove('bx-x');
    navbar.classList.remove('active');
}


/***************the book***************/
const pageTurnBtn = document.querySelectorAll('.nextprev-btn');

pageTurnBtn.forEach((el, index) => {
    el.onclick = () => {
        const pageTurnId = el.getAttribute('data-page');
        const pageTurn = document.getElementById(pageTurnId);

        if (pageTurn.classList.contains('turn')){
            pageTurn.classList.remove('turn');
            setTimeout(() => {
                pageTurn.style.zIndex = 20 - index;
            }, 500);
        }
        else
        pageTurn.classList.add('turn');
        setTimeout(() => {
            pageTurn.style.zIndex = 20 + index;
        }, 500);
    }
})

const pages = document.querySelectorAll('.book-page.page-right');

let totalPages = pages.length;
let pageNumber = 0;

function reverseIndex() {
    pageNumber--;
    if (pageNumber < 0){
        pageNumber = totalPages -1;
    }
}


//opening animation
const coverRight = document.querySelector('.cover.cover-right');

setTimeout(() => {
    coverRight.classList.add('turn');
},2100)

setTimeout(() => {
    coverRight.style.zIndex = -1;
},2800)

pages.forEach((_, index) =>{
    setTimeout(() => {
        reverseIndex();
        pages[pageNumber].classList.remove('turn');

        setTimeout(() =>{
            reverseIndex();
            pages[pageNumber].style.zIndex = 10 + index;
        }, 500)
    },(index + 1) * 200 + 2100)
})



//sign in
const logregBox = document.querySelector('.logreg-box');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');


registerLink.addEventListener('click', () => {
    logregBox.classList.add('active');
})


loginLink.addEventListener('click', () => {
    logregBox.classList.remove('active');
})

/*
//connect sign in to the chat page
function auth() {
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;

    if (email === 'mera@gmail.com' && password === '12345') {
        window.location.assign('file:///E:/Estidlal/Estedlale%20computation/intermediate-page/intermediate-page.html');
    } else {
        alert("Invalid info");
        return;
    }
}
*/
async function auth() {
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;

    try {
        const response = await fetch('http://localhost:3000/api/auth/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
        });

        if (response.ok) {
            const data = await response.json();
            // Redirect user to dashboard or another page upon successful login
            window.location.href = '#our services'; // Change '/dashboard' to your desired destination
        } else {
            // Handle failed login (e.g., show error message)
            const errorData = await response.json();
            alert(errorData.message);
        }
    } catch (error) {
        console.error('Error logging in:', error);
        // Handle network errors or other issues
        alert('An error occurred. Please try again later.');
    }
}

// Event listener for login button click
loginBtn.addEventListener('click', auth);


// Function to handle user registration
async function register() {
    var username = document.getElementById('username').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;

    try {
        const response = await fetch('http://localhost:3000/api/auth/register', { // Specify the correct URL for your backend register endpoint
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, email, password })
        });

        if (response.ok) {
            // Handle successful registration (e.g., show success message)
            alert('Registration successful. Please login to continue.');
            // Optionally, redirect user to the login page
            window.location.href = '#log-in'; // Redirect to login section
        } else {
            // Handle failed registration (e.g., show error message)
            const errorData = await response.json();
            alert(errorData.message);
        }
    } catch (error) {
        console.error('Error registering user:', error);
        // Handle network errors or other issues
        alert('An error occurred. Please try again later.');
    }
}

// Event listener for signup button click
signupBtn.addEventListener('click', register);




function validatePassword() {
        var password = document.getElementById("password1").value;
        if (password.length < 7) {
            alert("Password must be at least 8 characters long.");
            return false; // توقف عن إرسال النموذج
        }
        return true; // استمر في إرسال النموذج
}

// let alertBox = document.getElementById('alertBox');
// let LogInSuccessfully = '<i class="fa-sharp fa-solid fa-user-check"></i> Log in successfully';
// let LogInError = ' <i class="fa-solid fa-user-xmark"></i>  Please enter correct email and password'; 

// function error_message(msg){
//     let alertMessage = document.createElement('div');
    
//     alertMessage.classList.add('alertMessage');
//     alertMessage.innerHTML = msg;
//     alertBox.appendChild(alertMessage);

//     if(msg.includes('successfully')){
//         alertMessage.classList.add('successfully');
//     }

//     if(msg.includes('correct')){
//         alertMessage.classList.add('correct');
//     }

//     setTimeout(()=>{
//         alertMessage.remove();
//     },6000);
// }

// document.getElementById('showMessageButton').addEventListener('click', function() {
//     error_message(LogInSuccessfully);
//     error_message(LogInError);
// });

// function error_message(msg, type){
//     let alertBox = document.getElementById('alertBox');
//     let alertMessage = document.createElement('div');
//     alertMessage.classList.add('alertMessage');
//     alertMessage.innerHTML = msg;
//     alertBox.appendChild(alertMessage);

//     if(type === 'successfully'){
//         alertMessage.classList.add('successfully');
//     }

//     if(type === 'correct'){
//         alertMessage.classList.add('correct');
//     }

//     setTimeout(()=>{
//         alertMessage.remove();
//     }, 6000);
// }