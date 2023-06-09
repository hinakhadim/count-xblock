/* Javascript for HinaAIXBlock. */
function HinaAIXBlock(runtime, element) {

    function updateVotes(votes) {
        $('.upvote .count', element).text(votes.up);
        $('.downvote .count', element).text(votes.down);
    }

    var handlerUrl = runtime.handlerUrl(element, 'vote');

    $('.upvote', element).click(function (eventObject) {
        $.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify({ "voteType": "up" }),
            success: updateVotes
        });
    });

    $('.downvote', element).click(function (eventObject) {
        $.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify({ "voteType": "down" }),
            success: updateVotes
        });
    });


    $(function ($) {
        /* Here's where you'd do things on page load. */
    });
}
