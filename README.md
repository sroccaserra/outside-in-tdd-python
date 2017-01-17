From:

- <https://www.youtube.com/watch?v=XHnuMjah6ps>

## Problem description - Bank kata

Create a simple bank application with the following fetaures:

- Deposit into an Account
- Withdraw from an Account
- Print a bank statement to the console

## Acceptance criteria

Statement should have transactions in the following format:

```
> DATE       | AMOUNT  | BALANCE
> 10/04/2014 | 500.00  | 1400.00
> 02/04/2014 | -100.00 | 900.00
> 01/04/2014 | 1000.00 | 1000.00
```

## Starting point and constraints

1. Start with a class with the following structure:

```python
class Account:
    def deposit(self, amount):
        raise NotImplementedError()

    def withdraw(self, amount):
        raise NotImplementedError()

    def print_statement(self):
        raise NotImplementedError()

```

2. You are not allowed to add any other public method to this class.
3. Use Strings and Integers for dates and amounts (keep it simple)
4. Don't worry about spacing in the satement printed on the console

Note: the three public methods are commands, they don't return anything.

Note: I cannot add query methods, I cannot query for the state.

## Requirements

You need Python 3.4 or compatible. If you have pyenv installed, you can:

    $ make pyenv

Once you have a compatible version of Python installed, you can install the
requirements:

    $ make requirements

## Running the tests

See the `Makefile`.

## Notes

- deposit = dépôt, versement
- withdrawal = retrait
- balance = solde

- `Run` = `ctrl-R`
- `Run...` = `ctrl-alt-R`

### Présentation

- Bien expliquer la fonctionnalité au départ (souligner le mot de transaction,
  montrer l'ordre chronologique inverse)
- Commencer par écrire le feature test
- We need to identify the side effects, what are we testing in this acceptance
  test? Print this ordered transaction statements to the console. So that's
  what we should be testing for.
- Bien insister : on traite la console comme un système extérieur, comme on
  traiterait une base de données.
- External system ⇒ interface to isolate my application from the external
  world.

- Now that I know what the side effect is, I need to identify the trigger of
  the side effect.

### Account

- Why two methods: "I don't deposit -100, that doesn't make sense. Paying
  attention to that semantic is very important."
- Before I move on, I want to see my acceptance test fail for the right reason
  ⇒ remove `raise NotImplementedError()`
- Acceptance test fails for the right reason ⇒ time to park acceptance test
  (double loop of TDD)
- Why not inject console into account? I'm not quite sure that the account
  should call the console. I don't know how many abstractions will be between
  the account and the console.

### Go to unit level

- Simplest test I could possibly find. The deposit is an interesting candidate.
- All the methods in the account class are commands according to the initial
  constraints. I cannot change this interface.
- Problems with classic TDD : expose query methods for the purpose of testing.
- Storing total balance in account is not necessary for this feature.
- What is the side effect of a deposit? What do I want to happen when a deposit
  is made?
- I need to bind an amount to a date ⇒ transaction (montrer le README)
- Si date + amount + balance dans le même objet, si on reçoit les transactions
  dans le désordre (batches), il faut recalculer le solde des autres
  transactions (!)
- Design = trade-off
- Deposit = a lot of stuff: somehow get the current date, create transaction,
  store it... Defer some of it?
- The account itself shoud not know how the transaction is stored ⇒ repository
  pattern
- Dans le TU on mocke le `TransactionRepository`, pas dans l'acceptance test.

### Print statement

- Retour au test d'`Account`
- The `Account` class is a high level class, it should not know about the
  details of formating a statement.
- Bien passer par l'étape `statement_printer.print()` n'est jamais appelée dans
  les tests.
- Il y a eu beaucoup de décisions de design à cette étape.
- Pourquoi avoir créé une classe `Transaction` ? Parce que c'est ce qu'on veut
  imprimer, et c'est ce que stocke le `Transactionrepository`. Si on regarde
  les specs, ce sera surement l'association date / montant. 
- La classe `Account` est terminée, les méthodes sont au même niveau
  d'abstraction.
- What to do next ⇐ feature test failure.

### TransactionRepository

- In a real app, this would be an integrated test, inserting and querying the
  database. For the sake of this exercise, we create an in memory repository.
- Selon les specs, quand on store une transaction on doit stocker la date. Pour
  les tests, on doit contrôler les variables de type date, random, etc. On ne
  peut pas tester ce qu'on ne contrôle pas. La date système est quelque chose
  qu'on ne contrôle pas, elle change à chaque appel. On doit remplacer l'appel
  système par quelque chose qu'on contrôle. ⇒ `Clock`.
- Pas mal de décisions de design à cette étape.
- Dans le test d'acceptance, comme clock représente quelque chose d'extérieur
  au système qu'on ne contrôle pas et qu'on a besoin de contrôler, on mock la
  `Clock`.
- La classe `TransactionRepository` est terminée.

### Clock

- On isole l'effet de bord système au maximum, et on surcharge la méthode
  `today()` à l'ancienne (TDD classique).
- `Clock` done.

### StatementPrinter

- Retour aux specs, le plus simple est de commencer par le header avec une
  liste de transactions vide.


## Hindsights

- On a beaucoup parlé de design, plus que de test ou de qualité
- Les tests ont permis de retarder les décisions de design
    - Retarder les décisions de design a permis de faire des choix non pas au
      bon moment, mais au bon niveau d'abstraction ⇒ retarder non pas pour
      éviter de réfléchir, mais retarder quand ce n'est pas le bon niveau
      d'abstraction.
- On a pu définir le domaine sans se préoccuper du choix de la base de données.
- D'ailleurs on pourrait très facilement implémenter une persistance, ce qui
  poserait des questions de conf et de setup, mais on a pu travailler sur le
  domaine et la fonctionnalité en TU sans avoir à s'en préoccuper. 
- Les données persistées ne correspondent pas exactement aux classes du
  domaine.
- Les données lues dans la console ne correspondent pas exactement aux classes
  du domaine.

