"""
State - É um padrão de projeto comportamental que tem a 
intenção de permitir a um objeto mudar seu comportamento
quando seu estado interno muda.
O objeto parecerá ter mudado a sua classe.
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Order:
    # Context:
    def __init__(self) -> None:
        self.state: OrderState = PaymentPending(self)

    def pending(self) -> None:
        print('Triyng to execute the payment pending().')
        self.state.pending()
        print('State: ', self.state)
        print()

    def approve(self) -> None:
        print('Triyng to execute the payment approve().')
        self.state.approve()
        print('State: ', self.state)
        print()

    def reject(self) -> None:
        print('Triyng to execute the payment reject().')
        self.state.reject()
        print('State: ', self.state)
        print()


class OrderState(ABC):
    def __init__(self, order: Order) -> None:
        self.order = order
        
    @abstractmethod
    def pending(self)->None:
        print('Payment pending. You have to wait for the result. ')


    @abstractmethod
    def approve(self)->None:
        self.order.state = PaymentApproved(self.order)
        print('Payment Approved')


    @abstractmethod
    def reject(self)->None:
        self.order.state = PaymentRejected(self.order)
        print('Payment Rejected')

    def __str__(self) -> str:
        return self.__class__.__name__


class PaymentPending(OrderState):
    def pending(self)->None:
        print('Payment Pending.')

    
    def approve(self)->None:
        self.order.state = PaymentApproved(self.order)
        print('Payment approved.')


    def reject(self)->None:
        self.order.state = PaymentRejected(self.order)
        print('Payment Rejected')



class PaymentApproved(OrderState):
    def pending(self)->None:
        self.order.state = PaymentPending(self.order)
        print('Payment Pending.')


    def approve(self)->None:
        print('Payment already approved.')


    def reject(self)->None:
        self.order.state = PaymentRejected(self.order)
        print('Payment Rejected')



class PaymentRejected(OrderState):
    def pending(self)->None:
        print('Payment rejected.')


    def approve(self)->None:
        print('Payment rejected.')


    def reject(self)->None:
        print('Payment rejected.')

if __name__=='__main__':
    order = Order()
    order.pending()
    order.approve()
    order.pending()
    order.reject()
    order.pending()
    order.approve()
    