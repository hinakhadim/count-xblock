"""TO-DO: Write a description of what this XBlock is."""
import logging
import pkg_resources
from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Integer, Boolean, String, Scope

log = logging.getLogger(__name__)


class HinaAIXBlock(XBlock):
    """ Votes fields """

    upvote = Integer(default=0, scope=Scope.user_state_summary,
                     help='Number of up votes')
    downvote = Integer(default=0, scope=Scope.user_state_summary,
                       help='Number of down votes')
    votes = Boolean(default=False, scope=Scope.user_state,
                    help='Has this student voted?')
    text = String(default='', scope=Scope.user_state)

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        """
        The primary view of the HinaAIXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/hinaxblock.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/hinaxblock.css"))
        frag.add_javascript(self.resource_string(
            "static/js/src/hinaxblock.js"))
        frag.initialize_js('HinaAIXBlock')
        return frag

    @XBlock.json_handler
    def vote(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        if data['voteType'] not in ('up', 'down'):
            log.error('Vote Type is not known')
            return

        if data['voteType'] == 'up':
            self.upvote += 1
        if data['voteType'] == 'down':
            self.downvote += 1
        self.votes = True

        return {'up': self.upvote, 'down': self.downvote}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("HinaAIXBlock",
             """<hinaxblock/>
             """),
            ("Multiple HinaAIXBlock",
             """<vertical_demo>
                <hinaxblock/>
                <hinaxblock/>
                <hinaxblock/>
                </vertical_demo>
             """),
        ]
