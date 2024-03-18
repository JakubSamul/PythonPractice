// const h1 = document.createElement("h1")
// h1.textContent = "This is an imperative way to program"
// h1.className = "header"
// console.log(h1)


// JSX
// const page = (
//     <div>
//         <h1 className="header">This is JSX</h1>
//         <p>This is a paragraph</p>
//     </div>
// )

const navbar = (
    <nav>
        <h1>Jackobo Restaurant</h1>
        <li>Menu</li>
        <li>Drink</li>
        <li>Food</li>
    </nav>
)

ReactDOM.render(
    navbar,
    document.getElementById("root")
)