CREATE DATABASE IF NOT EXISTS livraria;

USE livraria;

CREATE TABLE IF NOT EXISTS livros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_livro VARCHAR(100) NOT NULL,
    nome_autor VARCHAR(50) NOT NULL,
    sexo_autor ENUM('MASCULINO', 'FEMININO') NOT NULL,
    paginas INT,
    nome_editora VARCHAR(100),
    valor DECIMAL(10,2),
    uf_editora CHAR(2),
    ano_publicacao YEAR
);

INSERT INTO livros (nome_livro, nome_autor, sexo_autor, paginas, nome_editora, valor, uf_editora, ano_publicacao) VALUES('Cavaleiro real', 'Ana Cláudia', 'FEMININO', 465, 'Atlas', 49.9, 'RJ', 2009);
INSERT INTO livros (nome_livro, nome_autor, sexo_autor, paginas, nome_editora, valor, uf_editora, ano_publicacao) VALUES('SQL para leigos', 'João Nunes', 'MASCULINO', 450, 'Addison', 98, 'SP', 2018);
INSERT INTO livros (nome_livro, nome_autor, sexo_autor, paginas, nome_editora, valor, uf_editora, ano_publicacao) VALUES('Receitas caseiras', 'Célia Tavares', 'FEMININO', 210, 'Atlas', 45, 'RJ', 2008);
INSERT INTO livros (nome_livro, nome_autor, sexo_autor, paginas, nome_editora, valor, uf_editora, ano_publicacao) VALUES('Pessoas efetivas', 'Eduardo Santos', 'MASCULINO', 390, 'Beta', 78.99, 'RJ', 2018);
INSERT INTO livros (nome_livro, nome_autor, sexo_autor, paginas, nome_editora, valor, uf_editora, ano_publicacao) VALUES('Hábitos saudáveis', 'Eduardo Santos', 'MASCULINO', 630, 'Beta', 150.98, 'RJ', 2019);
INSERT INTO livros (nome_livro, nome_autor, sexo_autor, paginas, nome_editora, valor, uf_editora, ano_publicacao) VALUES('A Casa Marrom', 'Hermes Macedo', 'MASCULINO', 250, 'Bubba', 60, 'MG', 2016);
INSERT INTO livros (nome_livro, nome_autor, sexo_autor, paginas, nome_editora, valor, uf_editora, ano_publicacao) VALUES('Estácio Querido', 'Geraldo Francisco', 'MASCULINO', 310, 'Insígnia', 100, 'ES', 2015);
INSERT INTO livros (nome_livro, nome_autor, sexo_autor, paginas, nome_editora, valor, uf_editora, ano_publicacao) VALUES('Pra sempre amigas', 'Leda Silva', 'FEMININO', 510, 'Insígnia', 78.89, 'ES', 2011);
INSERT INTO livros (nome_livro, nome_autor, sexo_autor, paginas, nome_editora, valor, uf_editora, ano_publicacao) VALUES('Copas Inesquecíveis', 'Marco Alcântara', 'MASCULINO', 200, 'Larson', 130.98, 'RS', 2018);  
INSERT INTO livros (nome_livro, nome_autor, sexo_autor, paginas, nome_editora, valor, uf_editora, ano_publicacao) VALUES('O poder da mente', 'Clara Mafra', 'FEMININO', 120, 'Continental', 56.36, 'RS', 2017);


SELECT nome_livro, nome_editora FROM livros;
SELECT nome_livro, nome_editora FROM livros;

SELECT nome_livro, uf_editora  FROM livros
WHERE sexo_autor = 'MASCULINO';

SELECT nome_livro, paginas FROM livros
WHERE sexo_autor = 'FEMININO';

SELECT * FROM livros
WHERE uf_editora = 'SP';

SELECT * FROM livros
WHERE sexo_autor = 'MASCULINO'
AND (uf_editora = 'RJ' OR uf_editora = 'SP');
