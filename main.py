from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import numpy as np
import joblib

class PricePredictionApp(App):
    def build(self):
        self.model = joblib.load('models/price_prediction_rf.pkl')
        
        # Main Layout
        main_layout = BoxLayout(orientation='vertical')
        
        # Input Fields
        features = [
            ("Battery (mAh)", int),
            ("No. of Processor", int),
            ("RAM (MB)", int),
            ("Storage (GB)", int),
            ("Rear Camera (px)", int),
            ("Front Camera (px)", int),
            ("Wifi (1 or 0)", bool),
            ("Bluetooth (1 or 0)", bool),
            ("GPS (1 or 0)", bool),
            ("No. of Sims", int),
            ("3G (1 or 0)", bool),
            ("4G (1 or 0)", bool),
            ("Resolution_y", int),
            ("Resolution_x", int)
        ]
        
        # Create input layouts for each feature
        for feature_name, data_type in features:
            input_layout = BoxLayout(orientation='horizontal')
            input_layout.add_widget(Label(text=f'{feature_name}:'))
            input_field = TextInput(hint_text=f'Enter {feature_name}')
            input_layout.add_widget(input_field)
            
            # Add input layout to the main layout
            main_layout.add_widget(input_layout)
        
        # Button
        button = Button(text='Predict')
        button.bind(on_press=self.predict)
        main_layout.add_widget(button)
        
        # Output Label
        self.output_label = Label(text='')
        main_layout.add_widget(self.output_label)
        
        return main_layout
    
    def predict(self, instance):
        # Get values from input fields and their types
        form_data = []
        for child in self.root.children:
            if isinstance(child, BoxLayout):
                input_field = None
                for widget in child.children:
                    if isinstance(widget, TextInput):
                        input_field = widget
                        break
                
                if input_field:
                    value = input_field.text.strip()
                    if value:
                        if input_field.hint_text.endswith('(1 or 0)'):
                            form_data.append(bool(int(value)))
                        else:
                            form_data.append(int(value))
                    else:
                        self.output_label.text = f'Please fill in all input fields'
                        return
                else:
                    continue
        
        # Make prediction if all fields are filled
        features = [np.array(form_data)]
        prediction = self.model.predict(features)
        self.output_label.text = 'Mobile price range should be {}'.format(prediction[0])

if __name__ == '__main__':
    PricePredictionApp().run()
