
// this function is used to get the answers for the requested question
function getAnswer() {
    $("#container").attr("hidden","true");
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
        if (response  =="no results found"){
        jQuery("#search_tag").text("No results found")
            jQuery("#header_space").attr("hidden","true")
            jQuery("#answer_space").attr("hidden","true")



        }
        else{
        var answers = JSON.parse(response);
        var text_area = $("#result_header");
        jQuery("#search_tag").text("Searched results are:")
            jQuery("#header_space").text("");
            jQuery("#answer_space").text("");
            headers_list = answers.headings;
            answers_list  = answers.answers;
            terms_list = answers.terms;

        // Displaying each heading of the answer
        jQuery.each(headers_list, function(i, item) {

            var header = headers_list[i].replace(/"|'/g, '\\"');
            var answer = answers_list[i].replace(/"|"/g,'\\"');

            var terms = terms_list[i]

            var arr = [];
            arr.push(terms_list[i]);

            var arr_string= JSON.stringify(arr);
            console.log(arr_string,"teeeeeeeeeeeeeeeeee")


            // on clicking this show answer() will be called and full answer will be displayed
            //text_area.append('<li class="p-5" title="Click Here To read complete Answer"' +
            //            ' onclick="showAnswer('+"'"+header+"'"+','+"'"+answer+"'"+',te'+""+')">'+header+'</li>');
            text_area.append("<li class='p-5' data-header='"+header+"' " +
                "data-arr='"+arr_string+"' data-ans='"+answer+"' title='Click Here To read complete Answer'>"+header+"</li>")

         });
        $(".p-5").on("click" ,function(){
            console.log(this);
            var _this = $(this);
            var arr = _this.data("arr");
            var ans = _this.data("ans");
            var header = _this.data("header");

           console.log(arr,"array of terms");

            var answer_space = $("#answer_space");
           var header_space = $("#header_space");
           answer_space.text(ans);
           header_space.text(header);
            var terms = arr[0];

            jQuery.each(terms, function(i, item) {

                var term = terms[i]
                 $("#answer_space:contains("+term+")").html(function(_, html) {

           return html.replace(new RegExp(term, 'g'), '<span class="p-6" data-term="'+term+'" ><b>'+term+'</b></span>');
           });


    });

    $('.p-6').on('click', function(){
        jQuery("#container").empty();
        var _this = $(this);
        var term = _this.data("term");


        jQuery.ajax({
        url: '/slm/getHeaders/',
        type: 'POST',
        data: {"term": term},
        datatype: "json",
        async: false
    }).done(function (response) {
            
            var headers = JSON.parse(response).headers
            var node = [];
            var edge = [];
            var dataset = {};

            var  _dict = {id:0,name:term,group:0}
            node.push(_dict);
            for(i in headers) {

                node.push({id: 1, name: headers[i], group: "1"})
                edge.push({relation:"Defined in",source: 0, target: 1,"group":1})
            }
            dataset.nodes = node;
            dataset.edges = edge;
            jQuery("#container").removeAttr("hidden");
            showGraph(dataset)



            })

        })
  })
        }


    })

}

