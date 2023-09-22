$(document).ready(function(){
    //downlaud data using APi and JQuery libreary
    $.get("https://my.api.mockaroo.com/Students.json?key=d9e2a660", function(data){
        //Bootstrap table
        $('table').bootstrapTable({
            data: data
        });
        //counting persons of each gender
        let male = 0;
        let female = 0;

        for (var person of data){
            if(person.gender == "Male"){
                male++;
            }else{
                female++;
            }
        }
      

        
        //Circle chart
        var barColors = [
            "#b91d47",
            "#1e7145"
        ];

        var genders = ["Male", "Female"];

        new Chart("firstChart", {
            type: "pie",
            data: {
                labels: genders,
                datasets: [{
                    backgroundColor: barColors,
                    data: [male,female]
                }]
            },
            options: {
                title: {
                    display: true,
                    text: "Number of students in each gender"
                }
            }
        });

        //Helpful function for counting partikular value in array
        Object.defineProperties(Array.prototype, {
            count: {
                value: function(value) {
                    return this.filter(x => x==value).length;
                }
            }
        });

        //Counting number of persons in each age
        let arr = [];

        for (var agee of data){
            arr.push(agee.age); 
         }

        //Linear chart
        var x_Values = ["17", "18", "19", "20", "21",'22', '23', '24'];
        let y_Values = [arr.count(17), arr.count(18), arr.count(19), arr.count(20), arr.count(21),arr.count(22),arr.count(23),arr.count(24)];
        var barColors = ["red", "green","blue","orange",'black','pink','purple','grey'];

        new Chart("secondChart", {
            type: "bar",
            data: {
                labels: x_Values,
                datasets: [{
                    backgroundColor: barColors,
                    data: y_Values
                }]
            },
            options: {           
                title: {
                display: true,
                text: "Number of student of each age"
                },
            
            scales: {
                yAxes: [{ticks: {min: 2, max:25}}]
            }
            }
        });
    });
  });
  

