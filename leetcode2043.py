class Bank:
  def __init__(self, balance: List[int]):
    self.balance = balance # self.balance 주소안에 balance 값이 있다. 
    
  def transfer(self, account1: int, account2: int, money: int) -> bool:
    if not self._isValid(account2): # 유효 함수가 아니면 
      return False
    return self.withdraw(account1, money) and self.deposit(account2, money)
#돈 전달함수는 account1 에서 돈 인출하고 account2에서 돈 입금


  def deposit(self, account: int, money: int) -> bool: #예금 함수 
    if not self._isValid(account): # 유효 함수가 아니면 
      return False
    self.balance[account - 1] += money  #integer array balance  끝 자리 업데이트 
    return True

# 계좌 넘버 int n 
  def withdraw(self, account: int, money: int) -> bool: #인출 함수 
    if not self._isValid(account):
      return False
    if self.balance[account - 1] < money: # 해당 머니에 충족이안되면 거짓 반대면 >=(less than or equal )
      return False
    self.balance[account - 1] -= money  #참이면 integer array balance  끝 자리 업데이트 
    return True

# The given account number(s) are between 1 and n 조건을 체크하는 함수 
  def _isValid(self, account: int) -> bool: # 유효 함수
    return 1 <= account <= len(self.balance)  