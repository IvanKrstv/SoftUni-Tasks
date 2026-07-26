function subtract() {
    const firstNumEl = document.getElementById('firstNumber').value
    const secondNumEl = document.getElementById('secondNumber').value

    const finalResult = Number(firstNumEl) - Number(secondNumEl)

    document.getElementById('result').textContent = finalResult
    
}