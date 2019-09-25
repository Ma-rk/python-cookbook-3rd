# introducing closure


class CompleteTemplateSentence:
    def __init__(self, template_sentence):
        self.template_sentence = template_sentence

    def execute_complete(self, **kwargs):
        return self.template_sentence.format_map(kwargs)


template_sentence = 'My name is {name}, I like {like}.'

template = CompleteTemplateSentence(template_sentence)
completed_sentence_1 = template.execute_complete(name='Mark', like='swimming')
print(completed_sentence_1)


def complete_template_sentence(template_sentence):
    def execute_complete(**kwargs):
        return template_sentence.format_map(kwargs)

    return execute_complete


closure_template = complete_template_sentence(template_sentence)
completed_sentence_2 = closure_template(name='Marc', like='swimming!!')
print(completed_sentence_2)
