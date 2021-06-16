$(document).ready(function(){
    $(".form-check").removeClass("form-check")
})
console.log("Hello Completed Project")

// $(document).ready(function() {


//     $(".btn-like").click(function(){

//         let response = fetch("http://127.0.0.1:8000/cards/api/2f1ee163-b97f-4da3-883a-40bf7953e00e").then((response) => response.json())


//         let btn_heart = $(".btn-like").children()

//         let classes = btn_heart.attr("class").split(" ")
//         for (let i = 0; i < classes.length; i++){
//             if (classes[i] === "animate__infinite" || btn_heart["heart_activated"] === "False"){
//                 btn_heart.removeClass("animate__animated animate__heartBeat animate__infinite")
//             }else{
//                 btn_heart.addClass(`animate__animated animate__heartBeat animate__infinite ${response}`)
//             }
//         }
//         // setTimeout(function(){
//         //     $(".btn-like").children().removeClass("animate__animated animate__heartBeat")
//         // }, 1000)

//     })

//     let children = $(".animate").children()

//     // $(".btn-submit").click(function(){
        
//     //     console.log($("input:text").val())
//     //     console.log($("input:email").val())
//     //     $(".btn-submit").get(0).type = 'submit'
//     // })


//     //custom Navbar Click
//     // $(".custom-navbar").children().click(function(){
//     //     document.location.href = "/"
//     // })
// })