import PredictScouter

from .MainWindow import MainWindow

predictor = PredictScouter.PredictScouter('sample_data.csv')

window = MainWindow()
window.mainloop()