class captions():
    def parse_captions(self, captions):
        self.captions = captions
        self.filter_caps = ''
        self.check_font = True
        for let in self.captions:
            if let == '<':
                self.check_font = False

            elif let == '>':
                self.check_font = True
            if let in '<>':
                continue

            if self.check_font == True:
                try:
                    int(let)
                except:
                    self.filter_caps += let

        self.filter_caps = self.filter_caps.replace('::, -- ::,', '')
        self.filter_caps = self.filter_caps.replace('\n\n\n', '\n')

        return self.filter_caps
