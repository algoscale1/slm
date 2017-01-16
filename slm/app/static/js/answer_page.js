


// this function is used to get the answwers for the requested question
function getAnswer() {

    jQuery(".mt-0 ").removeAttr("hidden");    // use to show "searched results are" above headings
    $("#result_header").find('li').remove() ;  // use to remove the headings for the answer
    $("#answer_space").contents().filter(function(){ return this.nodeType != 1; }).remove();     // use to remove headings+answer
    var requested_question = jQuery("#searchBar").val(); // get text of the search box
    jQuery.ajax({                              // request to the server for answers to the requested question
        url: '/slm/answers/',  //Server script to process data
        type: 'POST',
        data: {"question": requested_question},
        datatype: "json",
        async: false
    }).done(function (response) {

        var answers = JSON.parse(response);
        var text_area = $("#result_header");

        // Displaying each heading of the answer
            $.each(answers, function(header, answer) {
            answer = answer.replace(/'/g, "\\'");
            header = header.replace(/'/g, "\\'");
                // on clicking this show answer() will be called and full answer will be displayed
                text_area.append('<li class="p-5" title="Click Here To read complete Answer"' +
                        ' onclick="showAnswer('+"'"+header+"'"+','+"'"+answer+"'"+')">'+header+'</li>');
            });


    })

}


// this function is used to show a selected heading to its full answer.
function showAnswer(header, answer) {
           var answer_space = $("#answer_space");
           var header_space = $("#header_space");
           answer_space.text(answer)
           header_space.text(header)
}
