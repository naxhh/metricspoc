
class CommitAnalyzer:
    def __init__(self, reporter):
        self.reporter = reporter

    def analyze(self, repositories):
        for repository in repositories:
            self.reporter.report("Motor.Deploy.commits", repository)
