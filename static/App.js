// Actualizar un evento por ID
app.put('/eventos/:id', async (req, res) => {
    const eventId = req.params.id;

    try {
        const evento = await Evento.findByIdAndUpdate(eventId, req.body, { new: true });
        if (evento) {
            res.json(evento);
        } else {
            res.status(404).json({ message: 'Evento no encontrado' });
        }
    } catch (error) {
        res.status(400).json({ message: error.message });
    }
});
