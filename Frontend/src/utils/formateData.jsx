export const renderCell = (value) => {
    if (value !== undefined && value !== null && value !== '') {
        const datePattern = /^\d{4}-\d{2}-\d{2}$/;
        if (datePattern.test( value )) {

            const [year , month , day] = value.split( '-' );

            return `${day}.${month}.${year}`;
        }
        return value;
    } else {
        return <td style={{backgroundColor:'gray'}}></td>;
    }
};