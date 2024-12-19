class User:
    def __init__(self, name, cpf, age,serasa):
        self.name = name
        self.cpf = cpf
        self.balance = 0.0
        self.serasa = serasa
        self.transac_hist = []
        self.freq = {
            'daily_time': 0,
            'daily_bet_count': 0,
            'daily_spend': 0,
            'bet_total': 0,
            'spend_total': 0
        }
        self.total_money = 0
        self.age = age


    def add_balance(self, amount):
        self.balance += amount
        self.transac_hist.append(amount)
        self.total_money += amount


    def bet(self, amount):
        self.balance -= amount
        self.transac_hist.append(-amount)
        self.freq['spend_total'] += amount
        self.freq['bet_total'] += 1


    def win(self, amount):
        self.balance += amount
        self.transac_hist.append(amount)


    def set_transac_hist(self, transac_hist):
        self.transac_hist = transac_hist


    def set_freq(self, freq):
        self.freq = freq


    def get_user_profile(self):
        return (
            'Usuário: {}\n'
            'Idade: {}\n'
            'Média de tempo gasto na plataforma diariamente: {} minutos\n'
            'Quantidade média de apostas diárias: {}\n'
            'Valor médio gasto diariamente: R${}\n'
            'Número de apostas realizadas: {}\n'
            'Total gasto em apostas: R${}\n'
            'Saldo atual: R${}\n'
            'CPF: {}\n'
            'Usuário com nome sujo no Serasa: {}\n'
            'Histórico de transações: {}'
        ).format(
            self.name,
            self.age,
            self.freq['daily_time'],
            self.freq['daily_bet_count'],
            self.freq['daily_spend'],
            self.freq['bet_total'],
            self.freq['spend_total'],
            self.balance,
            self.cpf,
            'sim' if self.serasa else 'não',
            ' '.join(str(v) for v in self.transac_hist)
        )
