# Padrão MVC (Model-View-Controller)

## O que é o MVC?

O **MVC (Model-View-Controller)** é um **padrão de arquitetura de software** que separa uma aplicação em três camadas principais:

- **Model (Modelo)** → representa os **dados** e as **regras de negócio**.
- **View (Visão)** → é responsável pela **interface com o usuário** (entrada e saída de dados).
- **Controller (Controlador)** → atua como um **intermediário** entre o Model e a View, processando entradas e decidindo o que deve ser exibido.

O principal objetivo do MVC é **separar as responsabilidades**, facilitando a manutenção, o reuso e os testes do sistema.

---

## Funcionamento

1. O **usuário interage** com a **View** (por exemplo, digitando um dado ou clicando em um botão).
2. A **View** chama o **Controller**, que **processa a ação**.
3. O **Controller** atualiza o **Model** conforme necessário.
4. O **Model** notifica o **Controller** ou a **View** sobre as mudanças.
5. A **View** é **atualizada** com as novas informações do **Model**.

---

## Exemplo em Java

### Model.java
```java
public class Model {
    private String mensagem;

    public String getMensagem() {
        return mensagem;
    }

    public void setMensagem(String mensagem) {
        this.mensagem = mensagem;
    }
}
```

---

### View.java
```java
public class View {
    public void exibirMensagem(String mensagem) {
        System.out.println("Mensagem: " + mensagem);
    }
}
```

---

### Controller.java
```java
public class Controller {
    private Model model;
    private View view;

    public Controller(Model model, View view) {
        this.model = model;
        this.view = view;
    }

    public void setMensagem(String mensagem) {
        model.setMensagem(mensagem);
    }

    public void atualizarView() {
        view.exibirMensagem(model.getMensagem());
    }
}
```

---

### Main.java
```java
public class Main {
    public static void main(String[] args) {
        Model model = new Model();
        View view = new View();
        Controller controller = new Controller(model, view);

        controller.setMensagem("Olá, MVC em Java!");
        controller.atualizarView();
    }
}
```

---

## Fluxo de Execução

1. O **Main** cria as instâncias do `Model`, `View` e `Controller`.
2. O **Controller** define a mensagem no **Model**.
3. O **Controller** solicita à **View** que exiba a mensagem do **Model**.
4. A **View** exibe a mensagem no console.

---

## Benefícios do MVC

- **Separação de responsabilidades** (cada camada tem sua função).
- **Facilidade de manutenção e testes.**
- **Escalabilidade** — fácil adicionar novas Views ou modificar regras no Model.
- **Reutilização de código**.
