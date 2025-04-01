def story_prompt(protagonist: str, others: str):
    return f"""
        __ASK__
        Crie uma história de ninar para crianças com {protagonist} como protagonista e {others}.
        Extraia também uma lista de frases, de 5 a 10, para usar em ilustrações

        __CONSTRAINTS__
        - A história deve ter cerca de 700 palavras.
        - O final deve ser satisfatório e deixar o personagem principal em um lugar feliz
        - Muitas histórias de ninar terminam com um personagem principal abraçando um cuidador. Esta é uma ótima maneira de fazer uma criança dormir
        - Você quer envolver a criança e capturar sua imaginação, mas não quer que ela tenha que gastar muito poder cerebral seguindo a história. É uma habilidade complicada criar histórias vívidas com linguagem simples, mas com a prática você será capaz de conseguir isso
        - Muitas histórias clássicas de ninar terminam com o personagem principal aprendendo uma lição valiosa ou moral. Tente incorporar isso em seu conto também, mas escreva de uma forma que seja orgânica, não enfadonha
        - a linguagem deve em português do Brasil
        - Nunca utilize qualquer conteúdo inapropriado para crianças sobre nenhuma circunstância
        """
