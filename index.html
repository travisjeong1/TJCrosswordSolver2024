<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Crossword Solver</title>
    <!-- Include jQuery and jQuery UI -->
    <link rel="stylesheet" href="https://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
    <link rel="stylesheet" href="style.css">
    <style>
        .ui-datepicker {
            display: none;
            position: absolute;
            left: auto;
            right: 0;
        }
    </style>

    <script>
        $(function() {
            $("#date").datepicker({
                dateFormat: "yy-mm-dd",
                showOn: "focus",
                beforeShow: function(input, inst) {
                    var offset = $(input).offset();
                    var height = $(input).outerHeight();
                    window.setTimeout(function () {
                        inst.dpDiv.css({ // Make sure the calendar panel opens to the right of the text box
                            top: offset.top + height,
                            left: offset.left + $(input).outerWidth(),
                            right: 'auto'
                        });
                    }, 1);
                }
            });
        });

        function fetchResults() {
            var date = document.getElementById('date').value;
            fetch(`https://your-api-endpoint.com/api/solve/${date}`)
                .then(response => response.json())
                .then(data => {
                    window.location.href = `result.html?date=${date}`;
                })
                .catch(error => {
                    console.error('Error fetching results:', error);
                    alert('Failed to fetch results.');
                });
        }
    </script>
</head>
<body>
    <h1>&#129513; Welcome to CrosswordSolver! &#129513;</h1>
  
    <div class="box-container">
        <div class="todaybutton-container">
            <button onclick="window.location.href = '/solve_today';" class="today-button">Solve Today's Crossword</button>
        </div>
        <h2>Enter the date for the desired crossword puzzle</h2>
        <form id="date-form" onsubmit="event.preventDefault(); fetchResults();">
            <label for="date">Date (YYYY-MM-DD):</label>
            <input type="text" id="date" name="date" required autocomplete="off">
            <br>
            <button type="submit" class="solve-button">Solve</button>
        </form>
    </div>
</body>
</html>
