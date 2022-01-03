import React from 'react';

const SendBox = (props) => {
	return (
		<div className='col col-sm-3' >
			<input
				className='form-control'
				onKeyPress={(event) => event.key === 'Enter' && props.handleEmailSubmit(event.target.value)}
				placeholder='Enter email...'
			></input>
		</div>
	);
};

export default SendBox;
