import streamlit as st
import pandas as pd

def main():
    st.title('Combinar Archivos CSV usando DOI como referencia')
    
    st.write("Sube los dos archivos CSV que deseas combinar.")
    
    # Cargar archivos CSV
    file_1 = st.file_uploader("Sube el archivo 1 (CSV)", type=['csv'])
    file_2 = st.file_uploader("Sube el archivo 2 (CSV)", type=['csv'])
    
    if file_1 and file_2:
        try:
            # Leer los archivos CSV
            df1 = pd.read_csv(file_1)
            df2 = pd.read_csv(file_2)
            
            st.write("Vista previa del archivo 1:")
            st.dataframe(df1.head())
            
            st.write("Vista previa del archivo 2:")
            st.dataframe(df2.head())
            
            # Combinar los archivos usando la columna 'DOI'
            merged_df = pd.merge(df1, df2, on='DOI', how='outer')
            
            # Eliminar columnas duplicadas (si existen) 
            merged_df = merged_df.loc[:, ~merged_df.columns.duplicated()]
            
            # Mover la columna 'DOI' a la primera posición
            cols = list(merged_df.columns)
            cols.insert(0, cols.pop(cols.index('DOI')))
            merged_df = merged_df[cols]
            
            # Guardar el archivo combinado como match.csv
            merged_df.to_csv('match.csv', index=False)
            
            st.success("El archivo match.csv ha sido creado con éxito.")
            
            # Detectar y eliminar filas duplicadas (basadas en todas las columnas, excepto DOI) 
            duplicated_df = merged_df[merged_df.duplicated(subset=['DOI'], keep=False)]
            unique_df = merged_df.drop_duplicates(subset=['DOI'], keep='first')
            
            # Guardar los duplicados en un archivo llamado duplicado.csv
            duplicated_df.to_csv('duplicado.csv', index=False)
            
            st.success("El archivo duplicado.csv ha sido creado con éxito.")
            
            st.write("Vista previa de los datos combinados (sin duplicados):")
            st.dataframe(unique_df.head())
            
        except Exception as e:
            st.error(f"Ocurrió un error al procesar los archivos: {e}")
    else:
        st.info("Por favor, sube ambos archivos CSV para continuar.")

if __name__ == "__main__":
    main()
