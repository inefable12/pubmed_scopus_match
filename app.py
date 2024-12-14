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
            
            # Mover la columna 'DOI' a la primera posición para ambos DataFrames
            if 'DOI' in df1.columns:
                cols1 = list(df1.columns)
                cols1.insert(0, cols1.pop(cols1.index('DOI')))
                df1 = df1[cols1]
            
            if 'DOI' in df2.columns:
                cols2 = list(df2.columns)
                cols2.insert(0, cols2.pop(cols2.index('DOI')))
                df2 = df2[cols2]
            
            st.write("Vista previa del archivo 1:")
            st.dataframe(df1.head())
            
            st.write("Vista previa del archivo 2:")
            st.dataframe(df2.head())
            
            # Unir los archivos colocando primero el archivo 1 y luego el archivo 2
            combined_df = pd.concat([df1, df2], ignore_index=True)
            
            # Eliminar filas duplicadas basándose en la columna 'DOI'
            #combined_df = combined_df.drop_duplicates(subset=['DOI'], keep='first')
            
            # Mover la columna 'DOI' a la primera posición
            #cols = list(combined_df.columns)
            #cols.insert(0, cols.pop(cols.index('DOI')))
            #combined_df = combined_df[cols]
            
            # Guardar el archivo combinado como match.csv
            ##combined_df.to_csv('match.csv', index=False)
            
            #st.success("El archivo match.csv ha sido creado con éxito.")
            
            # Detectar y guardar las filas que estaban duplicadas antes de la eliminación
            #duplicated_df = pd.concat([df1, df2], ignore_index=True)
            #duplicated_df = duplicated_df[duplicated_df.duplicated(subset=['DOI'], keep=False)]
            
            # Guardar los duplicados en un archivo llamado duplicado.csv
            #duplicated_df.to_csv('duplicado.csv', index=False)
            
            #st.success("El archivo duplicado.csv ha sido creado con éxito.")
            
            #st.write("Vista previa de los datos combinados (sin duplicados):")
            st.dataframe(combined_df.head())
            
        except Exception as e:
            st.error(f"Ocurrió un error al procesar los archivos: {e}")
    else:
        st.info("Por favor, sube ambos archivos CSV para continuar.")

if __name__ == "__main__":
    main()
