from dash import Dash, html, dcc
import dash_ag_grid as dag
import pandas as pd
import numpy as np



# --color-dusty-rose-50: #f7eeed;
# --color-dusty-rose-100: #f0dcdb;
# --color-dusty-rose-200: #e1bab7;
# --color-dusty-rose-300: #d29793;
# --color-dusty-rose-400: #c3756f;
# --color-dusty-rose-500: #b4524b;
# --color-dusty-rose-600: #90423c;
# --color-dusty-rose-700: #6c312d;
# --color-dusty-rose-800: #48211e;
# --color-dusty-rose-900: #24100f;
# --color-dusty-rose-950: #190c0b;

# --color-linen-50: #fbf0ea;
# --color-linen-100: #f7e1d4;
# --color-linen-200: #eec3aa;
# --color-linen-300: #e6a57f;
# --color-linen-400: #dd8755;
# --color-linen-500: #d5692a;
# --color-linen-600: #aa5422;
# --color-linen-700: #803f19;
# --color-linen-800: #552a11;
# --color-linen-900: #2b1508;
# --color-linen-950: #1e0f06;

# --color-smoky-rose-50: #f5efef;
# --color-smoky-rose-100: #ebe0e0;
# --color-smoky-rose-200: #d8c0c1;
# --color-smoky-rose-300: #c4a1a1;
# --color-smoky-rose-400: #b08282;
# --color-smoky-rose-500: #9d6263;
# --color-smoky-rose-600: #7d4f4f;
# --color-smoky-rose-700: #5e3b3b;
# --color-smoky-rose-800: #3f2728;
# --color-smoky-rose-900: #1f1414;
# --color-smoky-rose-950: #160e0e;

# --color-pale-oak-50: #f7f4ee;
# --color-pale-oak-100: #efe8dc;
# --color-pale-oak-200: #dfd1b9;
# --color-pale-oak-300: #cfba96;
# --color-pale-oak-400: #bfa373;
# --color-pale-oak-500: #af8c50;
# --color-pale-oak-600: #8c7040;
# --color-pale-oak-700: #695430;
# --color-pale-oak-800: #463820;
# --color-pale-oak-900: #231c10;
# --color-pale-oak-950: #18140b;

# --color-taupe-50: #f4f2f0;
# --color-taupe-100: #e9e5e2;
# --color-taupe-200: #d3cac5;
# --color-taupe-300: #bdb0a8;
# --color-taupe-400: #a7958b;
# --color-taupe-500: #917b6e;
# --color-taupe-600: #746258;
# --color-taupe-700: #574a42;
# --color-taupe-800: #3a312c;
# --color-taupe-900: #1d1916;
# --color-taupe-950: #14110f;



app = Dash(
    __name__,
    external_scripts=["https://unpkg.com/@tailwindcss/browser@4"]
    )


df = pd.read_csv('Wine.csv')

dataset_info = {
    'Dataset Name':'Wine Quality Dataset (UCI Machine Learning Repository)',
    'Origin':'http://www.vinhoverde.pt/en/'
}


app.layout = html.Div(
    className='min-h-screen bg-slate-300 font-sans',
    children = [
        html.H1(
            children='Extensive Statistical Analysis of UCI Repo Wine Quality Dataset',
            className='bg-white text-3xl text-center font-black py-5 mb-4'
        ),
        html.Div(
            className = 'flex flex-col gap-5 px-3',
            children = [
                html.Div(
                    id = 'Dataset_Information',
                    
                    className = 'bg-white h-auto w-full rounded-xl px-3 py-2 ',
                    children = [
                        html.H3(
                            children='Dataset Information',
                            className='text-xl font-bold'
                                ),
                        html.Hr(),
                        html.Br(),
                        html.Ul([
                            html.Li(
                                children = [
                                    html.Span('Dataset Name : '),
                                    html.Br(),
                                    'Wine Quality Dataset (UCI Machine Learning Repository)'
                                ],
                                className='text-xl [&_span]:text-[17px]'
                            )
                        ]) 
                    ]
                        ),
                html.Div(
                    id = 'Data_View',
                    
                    className = 'rounded-xl bg-[#FCEADE] p-3',
                    children = [
                        
                        html.Div(
                            className = 'Data_view flex flex-col gap-3 [&_h1]:text-xl [&_h1]:font-bold [&_p]:font-bold',
                            children = [
                                html.H1('Dataset View'),
                                dag.AgGrid(
                                        id='data_table',
                                        rowData=df.to_dict('records'),
                                        columnDefs=[{'field':i} for i in df.columns],
                                        # columnSize="sizeToFit"
                                        ),
                                html.P('Dataset Shape :'),
                                html.P(f' {df.shape[0]} Observations, {df.shape[1]} Features')
                            ]
                        )
        
                    ]
                )
            ]
        )
        
        
    ]
)

if __name__ == '__main__':
    app.run(debug=True)