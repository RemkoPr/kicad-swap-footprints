import pcbnew

class ComponentSwap(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Swap the location of components"
        self.category = "Modify PCB"
        self.description = "Swap the coordinates of selected components"
        self.show_toolbar_button = True

    def Run(self):
        pcb = pcbnew.GetBoard()
        selected = [fp for fp in pcb.GetFootprints() if fp.IsSelected()]

        if len(selected) < 2:
            pcbnew.wxMessageBox("Select at least two components to swap.")
            return

        new_params = []
        for fp in selected:
            new_params.append({
                'pos': fp.GetPosition(),
                'orient': fp.GetOrientation(),
                'layer': fp.GetLayer(),
                'flip': fp.IsFlipped()
            })

        new_params = new_params[1:] + new_params[:1]

        for fp, params in zip(selected, new_params):
            fp.SetPosition(params['pos'])
            fp.SetOrientation(params['orient'])
            if fp.IsFlipped() != params['flip']:
                fp.Flip(fp.GetPosition())

        pcbnew.Refresh()

ComponentSwap().register()

