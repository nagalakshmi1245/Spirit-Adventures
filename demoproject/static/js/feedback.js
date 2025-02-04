// HAMBURGER NAVBAR

// Toggle the display of the navbar on hamburger click
const hamburger = document.getElementById("hamburger");
const mainList = document.getElementById("main_list");

hamburger.addEventListener("click", () => {
  mainList.classList.toggle("show");
});




// FEEDBACK

document.getElementById('feedbackForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting the traditional way

    // Get form values
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const feedback = document.getElementById('feedback').value;

    // Here you can send the data to your server or process it as needed
    // For demonstration, we'll just show a success message
    document.getElementById('responseMessage').innerText = 'Thank you for your feedback, ' + name + '!';
    document.getElementById('responseMessage2').innerText = 'Thank you for your info, ' + name + '!';
    
    // Clear the form
    document.getElementById('feedbackForm').reset();
});


// NAVBAR

// const navbar=document.querySelector(".navbar1");

// let lastScrollTop=0;

// window.addEventListener(
//     "scroll",()=>{
//         console.log("scroll");
//         var { scrollY }=window;
//         if (scrollY>lastScrollTop){
//             navbar.classList.remove("visible1");
//         }
//         elseif(scrollY < lastScrollTop); {
//             navbar.classList.add("visible1");
//         }
//         lastScrollTop=scrollY<=0?0:scrollY;
//     },
//     { passive:true }
// );