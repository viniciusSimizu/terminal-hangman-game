class Configuration:
    attempts: int = 6

    def set_attempts(self, attempts: int) -> 'Configuration':
        if attempts <= 0:
            print('Invalid!')
            return self

        self.attempts = attempts
        return self
