from ..models.gender import Gender

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..models.user import User
    from ..models.exercice import Exercice
    from ..models.exerciceToDo import ExerciceToDo

class Physics:
    __constante_gravity_terrestre = 9.81
    __muscle_efficy = 0.25  # from 0.2 to 0.25 depend on gender and age.

    @classmethod
    def __weightUse(cls, user: 'User', exo: 'Exercice', etc: 'ExerciceToDo') -> float:
        return (user.weight * exo.amplitude) + etc.additional_weight

    @classmethod
    def __quantityMovement(cls, exercice: 'Exercice', exercice_to_do: 'ExerciceToDo') -> float:
        return (
            (exercice_to_do.repetition * exercice_to_do.series) 
            if not exercice.is_minutes else
            ((exercice_to_do.repetition / 60) * 25 * exercice_to_do.series)
        )
    
    @classmethod
    def __muscleEfficyEval(cls, user: 'User') -> float:
        return (
            Physics.__muscle_efficy - 
            ( user.age / 2000 ) - 
            ( 0 if user.gender == Gender.Male else 0.01 )
        )
    
    @classmethod
    def evalJoulesUseForExercice(cls, user: 'User', exercice: 'Exercice', exercice_to_do: 'ExerciceToDo') -> float:
        print(f'--- {exercice.name} ---')
        print(f'weight : {Physics.__weightUse(user, exercice, exercice_to_do)}')
        print(f'quantity : {Physics.__quantityMovement(exercice, exercice_to_do)}')
        print(f'const : {(Physics.__constante_gravity_terrestre / (exercice_to_do.series**2))}')
        print(f'efficy : {Physics.__muscleEfficyEval(user)}')
        print(f'-----------------------')
        return (
            Physics.__weightUse(user, exercice, exercice_to_do) *
            Physics.__quantityMovement(exercice, exercice_to_do) *
            (Physics.__constante_gravity_terrestre / (exercice_to_do.series**2)) *
            Physics.__muscleEfficyEval(user) 
        )
    
    @classmethod
    def joulesToKcalories(cls, joules: float) -> float:
        return joules / 1000 # convertion brut for methabolisme (value mecanic : 4184).