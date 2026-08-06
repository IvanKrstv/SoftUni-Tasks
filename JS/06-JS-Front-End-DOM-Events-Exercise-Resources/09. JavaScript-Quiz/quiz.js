document.addEventListener('DOMContentLoaded', solve);

function solve() {
    const questions = Array.from(document.querySelectorAll('.question'));
    const resultBox = document.getElementById('results');
    const headingEl = document.querySelector('h1');

    const correctAnswers = [
        'onclick',
        'JSON.stringify()',
        'A programming API for HTML and XML documents'
    ];

    let rightAnswers = 0;

    function showQuestion(index) {
        questions.forEach((question, questionIndex) => {
            question.classList.toggle('hidden', questionIndex !== index);
        });
    }

    questions.forEach((question, index) => {
        const answers = question.querySelectorAll('.quiz-answer');

        answers.forEach((answer) => {
            answer.addEventListener('click', () => {
                if (answer.textContent === correctAnswers[index]) {
                    rightAnswers += 1;
                }

                if (index < questions.length - 1) {
                    showQuestion(index + 1);
                } else {
                    questions.forEach((section) => {
                        section.classList.add('hidden');
                    });

                    resultBox.textContent = rightAnswers === 3
                        ? 'You are recognized as top JavaScript fan!'
                        : rightAnswers === 1
                            ? `You have ${rightAnswers} right answer`
                            : `You have ${rightAnswers} right answers`;
                }
            });
        });
    });

    showQuestion(0);
}