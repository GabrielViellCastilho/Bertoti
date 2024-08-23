
"We see three critical differences between programming and software engineering: time, scale, and the trade-offs at play. On a software engineering project, engineers need to be more concerned with the passage of time and the eventual need for change. In a software engineering organization, we need to be more concerned about scale and efficiency, both for the software we produce as well as for the organization that is producing it. Finally, as software engineers, we are asked to make more complex decisions with higher-stakes outcomes, often based on imprecise estimates of time and growth."
----
Neste trecho explica que a diferença entre o programador e o engenheiro de software é que o engenheiro de software se preocupa com a estrutura do projeto, como a viabilidade de algum recurso, o prazo de entrega, e faz escolhas abrindo mão de outras oportunidades.

---
"Within Google, we sometimes say, “Software engineering is programming integrated over time.” Programming is certainly a significant part of software engineering: after all, programming is how you generate new software in the first place. If you accept this distinction, it also becomes clear that we might need to delineate between programming tasks (development) and software engineering tasks (development, modification, maintenance). The addition of time adds an important new dimension to programming. Cubes aren’t squares, distance isn’t velocity. Software engineering isn’t programming.
"
----
Nesta parte do texto, explica-se que o programador é a função que desenvolve o software, ou seja, a pessoa que escreve o código. Já o engenheiro de software vai além disso; além de escrever o código, ele também pensa na consistência do código, como a facilidade de modificações e de manutenção.

---
**Exemplos de Trade-offs:**
- Em uma aplicação em Spring Boot, é possível usar o Spring H2 Database, que salva os dados em memória, assim ganhando desempenho. Porém, a aplicação não pode ser interrompida. Por outro lado, há o MySQL Driver, que permite a integração do sistema Spring Boot com o MySQL, oferecendo uma melhor persistência de dados, porém com uma perda de desempenho.

- Em relação aos sistemas operacionais, há a comparação entre Linux e Windows. O Linux possui uma melhor estabilidade e performance, porém perde em usabilidade. Já o Windows possui uma melhor usabilidade devido à sua interface gráfica, mas perde em desempenho.

- Outro exemplo é a comparação entre bancos de dados SQL e NoSQL. No banco de dados SQL, há uma melhor integridade de dados, porém com perda de performance e flexibilidade. Já no NoSQL, obtém-se performance e flexibilidade, porém com perda na integridade dos dados.
---

Um exemplo de trade-off é a arquitetura de um sistema através de microserviços, que possui uma melhor escalabilidade e uma melhor manutenção do sistema. No entanto, aumenta a complexidade do sistema como um todo, como no caso do X (Twitter).

![Arquitetura Twitter](https://pbs.twimg.com/media/Fh8OE2jUAAEIVRR?format=jpg&name=4096x4096)

---
