var quiz = new Vue({
	delimiters: ['[[', ']]'],
    el: '#quiz',
    data: {
        timeLeft: 10,
        round: 1,
        latered: [],
        correct: 0,
        incorrect: 0,
    },

    mounted () {
        this.startTimer()
    },
    methods: {
        startTimer(){
          this.timerInterval = setInterval(() => {
                    this.timeLeft -= 1;
                    if (this.timeLeft == 0){
                        this.endQuiz();
                    }
          }, 1000);
        },
        later(){
            this.latered.push(this.round);
            this.round += 1;
        },
        endQuiz(){
            clearInterval(this.timerInterval);
        }
    }
});