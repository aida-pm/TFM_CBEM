
import glob 
import re

glob.glob(spath1+"\\*.stl")

vpath = 'E:\\Dades_TFM\\Images\\'
spath1 = 'E:\\Observer_1\\'
#spath2 = 'C:\\Users\\mreib\\OneDrive - upf.edu\\Burdeos\\Observer_2\\'

#output_path = 'C:\\Users\\mreib\\OneDrive - upf.edu\\Burdeos\\Segmentation mask\\'
output_path = 'E:\\Observer1\\'

mask1 = glob.glob(spath1+"\\*.stl")
#mask2 = glob.glob(spath2+"\\*.stl")

for i in range(0,len(mask1)):
#for i in range(0,2):	
	case =  re.sub("[^0-9]", "", mask1[i][-9:-6])
	volu_path = vpath + 'Case' + str(case) + '.mha'
	volume = slicer.util.loadVolume( volu_path, returnNode=True)
	segmentation1 = slicer.util.loadSegmentation(mask1[i],returnNode=True)
#	segmentation2 = slicer.util.loadSegmentation(mask2[i],returnNode=True)
	labelmapVolumeNode1 = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
#	labelmapVolumeNode2 = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
	ids1 = vtk.vtkStringArray()
#	ids2 = vtk.vtkStringArray()
	seg1 = getNode('case'+case+'_1')
#	seg2 = getNode('case'+case+'_2')
	seg1.GetDisplayNode().GetVisibleSegmentIDs(ids1)
#	seg2.GetDisplayNode().GetVisibleSegmentIDs(ids2)
	volume = seg1.GetNodeReference(slicer.vtkMRMLSegmentationNode.GetReferenceImageGeometryReferenceRole())
	slicer.modules.segmentations.logic().ExportSegmentsToLabelmapNode(seg1, ids1, labelmapVolumeNode1, volume)
#	slicer.modules.segmentations.logic().ExportSegmentsToLabelmapNode(seg2, ids2, labelmapVolumeNode2, volume)
	output1 = output_path + 'case'+ case + '_1.nii.gz'
#	output2 = output_path + 'case'+ case + '_2.nrrd'
	slicer.util.saveNode(labelmapVolumeNode1, output1)
#	slicer.util.saveNode(labelmapVolumeNode2, output2)


	vol=slicer.util.getNode('image*')
	slicer.mrmlScene.RemoveNode(vol)
	slicer.mrmlScene.RemoveNode(labelmapVolumeNode1)
	slicer.mrmlScene.RemoveNode(seg1)