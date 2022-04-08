const computerChoice = document.getElementById('computer-choice');
const userChoice = document.getElementById('user-choice');
const results = document.getElementById('result');
const possibleChoices = document.querySelectorAll('button');
let userChoices;
let compChoice;
let result

possibleChoices.forEach(possibleChoice => possibleChoice.addEventListener('click', (e) => {
    userChoices = e.target.id
    userChoice.innerHTML = userChoices
    generateCompChoice()
    getResult()
}))

function generateCompChoice() {
    const randomNumber = Math.floor(Math.random() * 3) + 1

    if (randomNumber === 1) {
        compChoice = 'rock'
    }
    if (randomNumber === 2) {
        compChoice = 'paper'
    }
    if (randomNumber === 3) {
        compChoice = 'scissors'
    }
    computerChoice.innerHTML = compChoice
}

function getResult() {
    if (compChoice === userChoices) {
        result = 'its a draw!'
    }
    if (compChoice === 'rock' && userChoices === 'paper') {
        result = 'you win'
    }
    if (compChoice === 'rock' && userChoices === 'scissors') {
        result = 'you lose'
    }
    if (compChoice === 'paper' && userChoices === 'scissors') {
        result = 'you win'
    }
    if (compChoice === 'paper' && userChoices === 'rock') {
        result = 'you lose'
    }
    if (compChoice === 'scissors' && userChoices === 'paper') {
        result = 'you lose'
    }
    if (compChoice === 'scissors' && userChoices === 'rock') {
        result = 'you win'
    }
    results.innerHTML = result
}