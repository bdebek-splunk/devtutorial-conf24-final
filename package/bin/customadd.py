import os, sys
from splunklib.searchcommands import dispatch, GeneratingCommand, Configuration, Option, validators

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))

@Configuration()
class CustomAdd(GeneratingCommand):

    first = Option(require=True, validate=validators.Integer(0))
    second = Option(require=True, validate=validators.Integer(0))

    def generate(self):

        # To connect with Splunk, use the instantiated service object which is created using the server-uri and
        # other meta details and can be accessed as shown below
        # Example:-
        #    service = self.service
        #    info = service.info //access the Splunk Server info

        self.logger.debug("Sum of %s and %s" , self.first, self.second)
        sum = int(self.first) + int(self.second)
        yield {'sum': sum}
         
if __name__ == "__main__":
    dispatch(CustomAdd, sys.argv, sys.stdin, sys.stdout, __name__)
