def wp_pragraph( p_text):

    code = f'<<!-- wp:paragraph --><p>{p_text}</p><!-- /wp:paragraph -->'
    return code
demo ="I want to be a part-time developer"
demo1 = 'I am not good at anything'
p=wp_pragraph(demo1)
print(p)
