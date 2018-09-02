import markdown


def article_pre_save(**kwargs):
    """ Compile markdown symbols to HTML """
    instance = kwargs['instance']
    instance.html_content = markdown.markdown(instance.content)
