# import the JSON utility package
import json
# import the Python math library
import math

# define the handler function that the Lambda service will use an entry point
def lambda_handler(event, context):
    val=int(event["value"])
    if event['input_scale'] == 'Celcius':
        if event['output_scale'] == 'Fahrenheit':
            result= val * 1.8 + 32
        elif event['output_scale'] == 'Kelvin':
            result= val + 273.15
        else:
            result= val
    elif event['input_scale'] == 'Fahrenheit':
        if event['output_scale'] == 'Celsius':
            result= (val - 32) / 1.8
        elif event['output_scale'] == 'Kelvin':
            result= (val + 459.67) * 5 / 9
        else:
            result= val
    elif event['input_scale'] == 'Kelvin':
        if event['output_scale'] == 'Celsius':
            result= val - 273.15
        elif event['output_scale'] == 'Fahrenheit':
            result= val * 9 / 5 - 459.67
        else:
            result= val
    else:
        result="select a value"
   
    # Convert the temperature and print the result
    return result 

    # return a properly formatted JSON object
    return {
    'statusCode': 200,
    'body': json.dumps(str(result))
    }