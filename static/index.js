const learnMoreButton = document.getElementById("learnMore");
const hideButton = document.getElementById("hide");

function learnMore() {
    learnMoreButton.removeEventListener("click", learnMore)
    learnMoreButton.innerHTML = `<ul style="list-style-position: inside; background-color: transparent;">
    <li>Surround phrases with quotes (") for exact match.</li>
    <li>Prepend words or phrases that must appear with a + symbol. Eg: +bitcoin</li>
    <li>Prepend words that must not appear with a - symbol. Eg: -bitcoin</li>
    <li>Alternatively you can use the AND / OR / NOT keywords, and optionally group these with parenthesis. Eg: crypto AND (ethereum OR litecoin) NOT bitcoin.</li>
    </ul>`;
    hideButton.style.display = "block";
    hideButton.addEventListener("click", hideEverything);
}

function hideEverything() {
    hideButton.style.display = "none";
    hideButton.removeEventListener("click", hideEverything)
    learnMoreButton.innerHTML = "Learn More!";
    learnMoreButton.addEventListener("click", learnMore)
}

learnMoreButton.addEventListener("click", learnMore)
hideButton.addEventListener("click", hideEverything)

